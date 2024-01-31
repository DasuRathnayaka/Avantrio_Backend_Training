import React from "react";
import { useModal } from "../../hooks/modalsHooks";

export default function ModalsExamplePage() {
    const { showModal } = useModal();
    return (
        <div className="container mt-5">
            <div className="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
                <h1 className="h2">Modals Example</h1>
            </div>

            <h2>Click the button below</h2>
            <button
                className="btn btn-primary"
                onClick={() => {
                    showModal({
                        modalType: "ExampleModalOne",
                        modalProps: { title: "Test Modal One" },
                    });
                }}
            >
                Show Modal
            </button>
        </div>
    );
}
