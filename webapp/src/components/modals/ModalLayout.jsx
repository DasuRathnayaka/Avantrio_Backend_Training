/*
Current modal layout logic is as follows.

Modal Layout has three sections; Header, Body, Footer
Make sure to include them within the ModalLayout Component in the correct order. (check one of the example modals)
You can render anything within those sections.
Modal layout takes the full screen hieght available while leaving padding on the top and bottom.
Within the Layout, Modal Header and Footer has fixed heights. 
Modal Boday takes up the full height avaialble regardless of the content height.
If the content within the Body compoent is too long, body component will be internally scrollable to view everything. (check ExampleModalOne)

Alternatively you can use just the Modal Layout without thoese three components if you need flexibility.

You can change these behaviours according the UI/UX design of the project. Plan these changes behaviors beforehand. 
Make sure that the changes are consistant across project and works well in any screen.
Do not chnage these components without consulting senior frontend engineers (someone equal or above SSE)
*/

function ModalLayout({ children }) {
    return (
        <div
            className="modal-dialog modal-dialog-scrollable m-0"
            style={{ width: 600 }}
        >
            <div className="modal-content h-100">{children}</div>
        </div>
    );
}

ModalLayout.Header = ({ children }) => (
    <div className="modal-header">
        <h5 className="modal-title w-100">{children}</h5>
    </div>
);

ModalLayout.Body = ({ children }) => (
    <div className="modal-body">{children}</div>
);

ModalLayout.Footer = ({ children }) => (
    <div className="modal-footer">{children}</div>
);

export default ModalLayout;
