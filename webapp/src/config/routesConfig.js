import AppLayout from "../components/AppLayout";
import SignInPage from "../pages/auth/SignInPage";
import SignoutPage from "../pages/auth/SignoutPage";

// example componets. remove after initialising a project.
import FormsExamplePage from "../pages/examples/FormsExamplePage";
import ModalsExamplePage from "../pages/examples/ModalsExample";
import TablesExamplePage from "../pages/examples/TablesExamplePage";
import RequireAuth from "../components/routing/PrivateRoute";
import PublicOnly from "../components/routing/PublicOnlyRoute";
import { getRouteObj } from "../utils/routeUtils";

export const routesConfig = [
    {
        title: "Home",
        path: "/app",
        element: (
            <RequireAuth>
                <AppLayout />
            </RequireAuth>
        ),
        routeId: "HOME",
        children: [
            {
                title: "Table",
                path: "tables",
                element: <TablesExamplePage />,
                routeId: "HOME_TABLE",
            },
            {
                title: "Form",
                path: "forms",
                element: <FormsExamplePage />,
                routeId: "HOME_FORM",
            },
            {
                title: "Modal",
                path: "modals",
                element: <ModalsExamplePage />,
                routeId: "HOME_MODAL",
            },
            {
                title: "Profile",
                path: "user/:id",
                element: <h3>My Account</h3>,
                routeId: "HOME_PROFILE",
            },
        ],
    },
    {
        title: "SignIn",
        path: "/signin",
        element: (
            <PublicOnly>
                <SignInPage />
            </PublicOnly>
        ),
        routeId: "SIGNIN",
    },
    {
        title: "Signout",
        path: "/signout",
        element: <SignoutPage />,
        routeId: "SIGNOUT",
    },
];

// Returns Route ID Dictionary
export const ROUTES = getRouteObj(routesConfig);
