import { useContext } from "react";
import { ModalContext } from "../providers/ModalProvider";

/**
 * Hook to access modal context actions that is used to `show` and `hide` modals. (Provides limited access)
 * @returns {{
 * showModal: ({ modalType: string, modalProps: any }) => void,
 * hideModal: () => void,
 * hideAllModals: () => void,
 * }}
 */
export const useModal = () => {
    const { showModal, hideModal, hideAllModals } = useContext(ModalContext);
    return { showModal, hideModal, hideAllModals };
};

/**
 * Hook to access modal context.
 * @returns {{
 * modalTypes: string[],
 * modalProps: any,
 * showModal: ({ modalType: string, modalProps: any }) => void,
 * hideModal: () => void,
 * hideAllModals: () => void,
 * }}
 */
export const useModalContext = () => useContext(ModalContext);
