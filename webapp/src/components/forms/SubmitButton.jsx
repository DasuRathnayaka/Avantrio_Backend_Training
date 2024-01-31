import React from "react";
import { useFormikContext } from "formik";
import Button from "../Button";

/**
 * Submit button integrated with Formik.
 * @param {{
 * children: JSX.Element,
 * size: "sm" | "lg",
 * variant: "primary" | "secondary" | "outline-primary" | "outline-secondary",
 * fullWidth: boolean,
 * }} props
 * @returns {React.FunctionComponent}
 */
export default function SubmitButton({
    children = "Submit",
    size,
    variant,
    fullWidth = true,
}) {
    const { isSubmitting } = useFormikContext();
    return (
        <Button
            type="submit"
            isLoading={isSubmitting}
            disabled={isSubmitting}
            size={size}
            variant={variant}
            fullWidth={fullWidth}
        >
            {children}
        </Button>
    );
}
