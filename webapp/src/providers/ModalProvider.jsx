import { createContext, useState } from "react";

export const ModalContext = createContext({
    modalTypes: [], // stack
    modalProps: {},
    showModal: () => {},
    hideModal: () => {},
    hideAllModals: () => {},
});

export default function ModalProvider({ children }) {
    const [modalTypes, setModalTypes] = useState([]);
    const [modalPropsByModalType, setModalPropsByModalType] = useState({});

    const showModal = ({ modalType, modalProps }) => {
        const modifiedModalProps = { ...modalPropsByModalType };
        const modifiedModalTypes = [...modalTypes];
        modifiedModalProps[modalType] = modalProps;
        modifiedModalTypes.push(modalType);
        setModalPropsByModalType(modifiedModalProps);
        setModalTypes(modifiedModalTypes);
    };

    const hideModal = () => {
        const modifiedModalTypes = [...modalTypes];
        const removedModalType = modifiedModalTypes.pop();
        setModalTypes(modifiedModalTypes);
        return removedModalType;
    };

    const hideAllModals = () => {
        setModalPropsByModalType({});
        setModalTypes([]);
    };
    return (
        <ModalContext.Provider
            value={{
                modalTypes,
                modalProps: modalPropsByModalType,
                showModal,
                hideModal,
                hideAllModals,
            }}
        >
            {children}
        </ModalContext.Provider>
    );
}
