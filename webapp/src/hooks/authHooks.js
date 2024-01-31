import { ACCESS_TOKEN_NAME } from "../constants";

export const useLoginStatus = () => {
    if (sessionStorage.getItem(ACCESS_TOKEN_NAME)) {
        return true;
    }
    return false;
};
