import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";

export default function SignoutPage() {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    useEffect(() => {
        // clear redux store
        dispatch({ type: "auth/logout" });
        // clear browser storages
        localStorage.clear();
        sessionStorage.clear();
        //go to signin page
        navigate("/signin");
    }, [dispatch, navigate]);

    return null;
}
