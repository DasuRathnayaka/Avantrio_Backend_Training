import React from "react";
import { useField } from "formik";

/**
 * Native `text` input wrapper with Formik integration.
 * @param {{
 * name: string,
 * label: string,
 * placeholder?: string,
 * type?: string,
 * disabled?: boolean
 * }} props
 * @returns {React.FunctionComponent}
 */
export default function TextField({
    name,
    label,
    type = "text",
    placeholder,
    ...rest
}) {
    const [field, meta] = useField({ name, label, type, placeholder, ...rest });
    return (
        <div className="w-100">
            {label && (
                <label htmlFor={name} className="form-label">
                    {label}
                </label>
            )}
            <input
                className="form-control"
                placeholder={placeholder || ""}
                type={type}
                {...field}
                {...rest}
            />

            <div
                hidden={!(meta.touched && meta.error)}
                className="invalid-feedback"
                style={{ display: "block" }}
            >
                {meta.error}
            </div>
        </div>
    );
}
