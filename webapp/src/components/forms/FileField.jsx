import React from "react";
import { useField } from "formik";
// TODO: show selected file name and other UI feedback

/**
 * Native HTML `file` input with Formik integration.
 * @param {{
 * name: string
 * label: string
 * disabled ?: boolean
 * }} props
 * @returns {React.FunctionComponent}
 */
export default function FileField(props) {
    const { name, label, ...rest } = props;
    const [, meta, helpers] = useField(props);
    return (
        <>
            {label && <label htmlFor={name}>{label}</label>}
            <input
                {...rest}
                type="file"
                onChange={(e) => helpers.setValue(e.currentTarget.files[0])}
                className="form-control"
            />
            {meta.touched && meta.error ? (
                <div className="invalid-feedback" style={{ display: "block" }}>
                    {meta.error}
                </div>
            ) : null}
        </>
    );
}
