import React from "react";
import { Field, ErrorMessage } from "formik";

/**
 * Native `radio` input for boolean selections. Integrated with Formik.
 * @param {{
 * name: string,
 * label: string,
 * }} props
 * @returns
 */
export default function YesNoRadio(props) {
    const { name, label } = props;

    return (
        <Field name={name} id={name} label={label}>
            {({ field, form: { setFieldValue } }) => (
                <div>
                    {/* <label>{label}</label> */}
                    <div className="d-flex">
                        <div className="custom-control custom-radio mr-3">
                            <input
                                className="custom-control-input"
                                checked={field.value}
                                onChange={() => {
                                    setFieldValue(name, true);
                                }}
                                id={`${name}-yes`}
                                type="radio"
                            />
                            <label
                                className="custom-control-label"
                                htmlFor={`${name}-yes`}
                            >
                                Yes{" "}
                            </label>
                        </div>
                        <div className="custom-control custom-radio">
                            <input
                                className="custom-control-input"
                                checked={field.value === false}
                                onChange={() => {
                                    setFieldValue(name, false);
                                }}
                                id={`${name}-no`}
                                type="radio"
                            />
                            <label
                                className="custom-control-label"
                                htmlFor={`${name}-no`}
                            >
                                No{" "}
                            </label>
                        </div>
                    </div>
                    <ErrorMessage
                        name={name}
                        render={(msg) => (
                            <div style={{ color: "red" }}>{msg}</div>
                        )}
                    />
                </div>
            )}
        </Field>
    );
}
