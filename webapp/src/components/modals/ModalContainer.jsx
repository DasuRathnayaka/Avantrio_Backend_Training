/*
Modals can be stackable.
When hiding stacked modals the top-most one will go out first.(LIFO)
Show/hide functionality will be handled via a custom hook. (check modalHooks)
Modals will blur the backgrounds. Clicking on the background won't close the modal.

Edit below component to change these beaviours. Make sure to consult an SSE or above rank before making changes.
*/

import { useContext } from "react";
import { ModalContext } from "../../providers/ModalProvider";

import ExampleModalOne from "../examples/ExampleModalOne";
import ExampleModalTwo from "../examples/ExampleModalTwo";
import "./modal-container.scss";

// register modals here.
const modalContent = {
    ExampleModalOne,
    ExampleModalTwo,
};

export default function ModalContainer() {
    const { modalProps, modalTypes, hideModal } = useContext(ModalContext);

    const handleClose = async () => {
        // hide current modal
        await hideModal();
    };

    return modalTypes.map((modalType) => {
        const CurrModalContent = modalContent[modalType];
        const currModalProps = { ...modalProps[modalType] };
        if (currModalProps && !currModalProps.closeModal) {
            currModalProps.closeModal = handleClose;
        }

        return (
            <div
                className="modal-container"
                id="exampleModal"
                tabIndex="-1"
                aria-labelledby="exampleModalLabel"
                aria-hidden="true"
            >
                <CurrModalContent {...currModalProps} />
            </div>
        );
    });
}
