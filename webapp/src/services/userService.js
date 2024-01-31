import { createApi } from "@reduxjs/toolkit/query/react";
import { baseQueryWithReauth } from "./baseQueries";
export const userAPI = createApi({
    reducerPath: "userAPI",
    baseQuery: baseQueryWithReauth,
    endpoints: (build) => ({
        getMyProfile: build.query({
            query: () => ({
                url: `/api/users/me/`,
            }),
        }),
    }),
});

export const { useGetMyProfileQuery } = userAPI;
