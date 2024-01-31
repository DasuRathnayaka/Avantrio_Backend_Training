import { fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import { Mutex } from "async-mutex";
import { ACCESS_TOKEN_NAME, REFRESH_TOKEN_NAME } from "../constants";

export const publicBaseQuery = fetchBaseQuery({
    baseUrl: process.env.REACT_APP_API_BASE,
});

const baseQueryWithAuthHeaders = fetchBaseQuery({
    baseUrl: process.env.REACT_APP_API_BASE,
    prepareHeaders: (headers) => {
        const token = sessionStorage.getItem(ACCESS_TOKEN_NAME);
        if (token) {
            headers.set("Authorization", `Bearer ${token}`);
        }
        return headers;
    },
});
// create a new mutex
const mutex = new Mutex();
export const baseQueryWithReauth = async (args, api, extraOptions) => {
    // wait until the mutex is available without locking it
    await mutex.waitForUnlock();
    let result = await baseQueryWithAuthHeaders(args, api, extraOptions);
    if (result.error && result.error.status === 401) {
        // checking whether the mutex is locked
        if (!mutex.isLocked()) {
            const release = await mutex.acquire();
            try {
                const refreshResult = await baseQueryWithAuthHeaders(
                    {
                        url: "/api/auth/token/refresh/",
                        method: "POST",
                        body: {
                            refresh:
                                sessionStorage.getItem(REFRESH_TOKEN_NAME) ||
                                localStorage.getItem(REFRESH_TOKEN_NAME),
                        },
                    },
                    api,
                    extraOptions,
                );
                if (refreshResult.data) {
                    // save new access token
                    sessionStorage.setItem(
                        ACCESS_TOKEN_NAME,
                        refreshResult.data.data?.access,
                    );
                    // retry the initial query
                    result = await baseQueryWithAuthHeaders(
                        args,
                        api,
                        extraOptions,
                    );
                } else {
                    window.location = "/signout";
                }
            } finally {
                // release must be called once the mutex should be released again.
                release();
            }
        } else {
            // wait until the mutex is available without locking it
            await mutex.waitForUnlock();
            result = await baseQueryWithAuthHeaders(args, api, extraOptions);
        }
    }
    return result;
};
