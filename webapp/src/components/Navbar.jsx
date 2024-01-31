import React from "react";
import { Link } from "react-router-dom";
import { ROUTES } from "../config/routesConfig";
import { useRouting } from "../hooks/routesHooks";
import { APP_NAME } from "../config/appConfig";
import "./navbar.scss";

export default function Navbar() {
    const { getRouteLink } = useRouting();

    return (
        <header className="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0 shadow">
            <Link
                className="navbar-brand col-md-3 col-lg-2 me-0 px-3"
                to={getRouteLink(ROUTES.HOME)}
            >
                {APP_NAME}
            </Link>
            <button
                className="navbar-toggler position-absolute d-md-none collapsed"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#sidebarMenu"
                aria-controls="sidebarMenu"
                aria-expanded="false"
                aria-label="Toggle navigation"
            >
                <span className="navbar-toggler-icon"></span>
            </button>
            <div className="navbar-nav">
                <div className="nav-item text-nowrap">
                    <Link
                        className="nav-link px-3"
                        to={getRouteLink(ROUTES.SIGNOUT)}
                    >
                        Sign out
                    </Link>
                </div>
            </div>
        </header>
    );
}
