import React from "react";
import { Link } from "react-router-dom";
import { useRouting } from "../hooks/routesHooks";

function Breadcrumbs() {
    const { breadcumbPath } = useRouting();

    return (
        <div className="mt-4">
            {breadcumbPath.map((active, index, { length }) => (
                <span key={index}>
                    {index === 0 ? "" : " > "}
                    {index !== length - 1 ? (
                        <Link to={active.match.pathname}>{active.title}</Link>
                    ) : (
                        <>{active.title}</>
                    )}
                </span>
            ))}
        </div>
    );
}

export default Breadcrumbs;
