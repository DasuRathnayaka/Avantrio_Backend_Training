import { useEffect, useState } from "react";
import { generatePath, useLocation, matchPath } from "react-router-dom";
import { routesConfig as routes } from "../config/routesConfig";

export const useRouting = () => {
    const { pathname } = useLocation();

    const [breadcumbPath, setBreadcumbPath] = useState([]);

    useEffect(() => {
        mapDefinitionToActivePath(routes, pathname);
    }, [pathname]);

    let activeRoutePaths = [];

    const mapDefinitionToActivePath = (definitions, pathname, parentPath) => {
        definitions?.forEach((definition) => {
            const pathPatternWithParent = concatPaths(
                parentPath,
                definition.path,
            );
            const match = matchPatternInPath(pathPatternWithParent, pathname);

            if (!match) {
                return;
            }
            if (
                isPathActiveForLocation(match.pathname, pathname) &&
                definition.path !== "*"
            ) {
                const activeRoutePath = {
                    definition: definition,
                    title: definition.title,
                    match: match,
                };

                addActiveRoutePathIfPossible(activeRoutePaths, activeRoutePath);

                if (definition.children) {
                    const nestedMatches = mapDefinitionToActivePath(
                        definition.children,
                        pathname,
                        pathPatternWithParent,
                    );
                    nestedMatches?.forEach((activePath) => {
                        addActiveRoutePathIfPossible(
                            activeRoutePaths,
                            activePath,
                        );
                    });
                }

                setBreadcumbPath(activeRoutePaths);
            }
        });
    };

    function matchPatternInPath(
        pathPattern,
        locationPathname,
        requireExactMatch = false,
    ) {
        return matchPath(
            {
                path: pathPattern,
                end: requireExactMatch,
            },
            locationPathname,
        );
    }

    function isPathActiveForLocation(pathName, locationPathname) {
        return (
            locationPathname === pathName ||
            (locationPathname.startsWith(pathName) &&
                locationPathname.charAt(pathName.length) === "/")
        );
    }

    function concatPaths(parent, current) {
        const joinPaths = (paths) => paths.join("/").replace(/\/\/+/g, "/");

        const jointPaths = joinPaths([parent, current]);
        return jointPaths;
    }

    function addActiveRoutePathIfPossible(activeRoutePaths, activePath) {
        if (canBeAddedToActiveRoutes(activeRoutePaths, activePath.match)) {
            activeRoutePaths.push(activePath);
        }
    }

    const canBeAddedToActiveRoutes = (activeRoutePaths, match) => {
        return (
            isNotSameAsPreviousMatch(activeRoutePaths, match) &&
            isMoreSpecificThanPreviousMatch(activeRoutePaths, match.pathname)
        );
    };

    const getPreviousMatch = (previousMatches) => {
        return previousMatches[previousMatches.length - 1];
    };

    const isNotSameAsPreviousMatch = (previousMatches, match) => {
        const previousMatchedPathname =
            getPreviousMatch(previousMatches)?.match.pattern ?? "";
        return previousMatchedPathname !== match.pattern;
    };

    const isMoreSpecificThanPreviousMatch = (previousMatches, toPathname) => {
        const previousMatchedPathname =
            getPreviousMatch(previousMatches)?.match.pathname ?? "";
        return toPathname.length > previousMatchedPathname.length;
    };

    const getRouteLink = (routeId, params = {}) => {
        const getPath = (routes, routeId) => {
            for (let item of routes) {
                if (item.routeId === routeId) return `${item.path}`;
                if (item.children) {
                    const child = getPath(item.children, routeId);
                    if (child) return `${item.path}/${child}`;
                }
            }
        };

        const path = getPath(routes, routeId);
        const generatedPath = generatePath(path, params);
        return generatedPath;
    };

    return {
        getRouteLink,
        breadcumbPath,
        activePath: pathname,
    };
};
