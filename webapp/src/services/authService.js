import { createApi } from "@reduxjs/toolkit/query/react";
import { publicBaseQuery } from "./baseQueries";
export const authAPI = createApi({
    reducerPath: "authAPI",
    baseQuery: publicBaseQuery,
    endpoints: (build) => ({
        signIn: build.mutation({
            query: ({ username, password }) => ({
                url: `/api/auth/token/`,
                method: "POST",
                body: { username, password },
            }),
        }),
    }),
});

export const { useSignInMutation } = authAPI;
