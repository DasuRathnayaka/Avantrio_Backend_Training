import React from "react";
import { Formik, Form as FormikForm } from "formik";

/**
 * Wrapper for Formik `Form` with `onSubmit` handler. Uses Formik context.
 * @param {{
 * initialValues: any,
 * validationSchema?: string,
 * enableReinitialize?: boolean,
 * className: string,
 * onSubmit: (changedValues: any) => void,
 * children: JSX.Element,
 * }} props
 * @returns {React.FunctionComponent}
 */
export default function Form({
    children,
    initialValues,
    validationSchema,
    enableReinitialize,
    className,
    onSubmit,
    ...rest
}) {
    return (
        <Formik
            initialValues={initialValues}
            validationSchema={validationSchema}
            onSubmit={onSubmit}
            enableReinitialize={enableReinitialize}
            {...rest}
        >
            <FormikForm className="needs-validation w-100" noValidate="">
                {children}
            </FormikForm>
        </Formik>
    );
}
