import { configureStore, combineReducers } from "@reduxjs/toolkit";
import { counterReducer } from "./services/counterService";
import { authAPI } from "./services/authService";
import { userAPI } from "./services/userService";

const combinedReducer = combineReducers({
    counter: counterReducer, //TODO: sample service. remove in actual projects
    [authAPI.reducerPath]: authAPI.reducer,
    [userAPI.reducerPath]: userAPI.reducer,
    // ... add your reducers here
});

// we structure store like this so that we can easily reset the store on logout.
const rootReducer = (state, action) => {
    if (action.type === "auth/logout") {
        state = undefined;
    }
    return combinedReducer(state, action);
};

export const store = configureStore({
    reducer: rootReducer,
    //add rtkq middleware to below aray
    middleware: (getDefaultMiddleware) =>
        getDefaultMiddleware()
            .concat(authAPI.middleware)
            .concat(userAPI.middleware),
    devTools: true,
});
