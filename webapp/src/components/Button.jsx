import React from "react";

/**
 * Native button wrapped to enable customization with bootstrap sizes and variants
 * @param {{
 * children: JSX.Element,
 * size: "sm" | "lg",
 * variant: "primary" | "secondary" | "outline-primary" | "outline-secondary",
 * type: "button" | "submit",
 * disabled: boolean,
 * fullWidth: boolean,
 * isLoading: boolean
 * }} props
 * @returns {React.FunctionComponent}
 */
export default function Button({
    type = "button",
    disabled = false,
    children = "Button",
    size = "",
    variant = "primary",
    fullWidth = true,
    isLoading = false,
}) {
    const getButtonClassName = () => {
        const btnClasses = ["", "", ""];

        if (size && typeof size === "string") {
            btnClasses[0] = `btn-${size}`;
        }
        if (typeof variant === "string") {
            btnClasses[1] = `btn-${variant}`;
        }
        if (fullWidth) {
            btnClasses[2] = "w-100";
        }
        return `btn ${btnClasses.join(" ")}`;
    };

    return (
        <button
            type={type}
            className={getButtonClassName()}
            disabled={disabled}
            aria-label="button"
        >
            {isLoading ? (
                <>
                    <span
                        className="spinner-border spinner-border-sm"
                        role="status"
                        aria-hidden="true"
                    ></span>
                    <span className="ms-2">Loading...</span>
                </>
            ) : (
                children
            )}
        </button>
    );
}
