import { useRoutes } from "react-router-dom";

function RoutesRender({ routes }) {
    const renderedRoutes = useRoutes(routes);
    return renderedRoutes;
}

export default RoutesRender;
