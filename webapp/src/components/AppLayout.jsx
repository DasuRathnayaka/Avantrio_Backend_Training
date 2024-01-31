import React from "react";
import { Outlet } from "react-router-dom";
import Breadcrumbs from "./Breadcrumbs";
import Navbar from "./Navbar";
import Sidebar from "./Sidebar";

export default function AppLayout() {
    return (
        <div>
            <Navbar />
            <div className="container-fluid">
                <div className="row">
                    <Sidebar />
                    <main className="col-md-9 ms-sm-auto col-lg-10 px-md-4">
                        <Breadcrumbs />
                        <Outlet />
                    </main>
                </div>
            </div>
        </div>
    );
}
