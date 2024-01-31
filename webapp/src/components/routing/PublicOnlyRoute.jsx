import React from "react";
import { Navigate } from "react-router-dom";
import { ROUTES } from "../../config/routesConfig";
import { useLoginStatus } from "../../hooks/authHooks";
import { useRouting } from "../../hooks/routesHooks";
import ScrollToTop from "./ScrollTop";

const PublicOnly = ({
    redirectTitle = ROUTES.SIGNIN,
    scrollToTop = true,
    children,
}) => {
    const isLoggedIn = useLoginStatus();
    const { getRouteLink } = useRouting();

    // Show the component only when the user is logged in
    // Otherwise, redirect the user to home page

    if (isLoggedIn) {
        return (
            <>
                {scrollToTop && <ScrollToTop />}{" "}
                <Navigate to={getRouteLink(redirectTitle)} replace />
            </>
        );
    }

    return (
        <>
            {scrollToTop && <ScrollToTop />} {children}
        </>
    );
};

export default PublicOnly;
