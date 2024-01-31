import ModalContainer from "./components/modals/ModalContainer";
import "./custom.scss";
import { routesConfig } from "./config/routesConfig";
import RoutesRender from "./components/routing/RoutesRender";

function App() {
    return (
        <div className="App">
            <ModalContainer />
            <RoutesRender routes={routesConfig} />
        </div>
    );
}

export default App;
