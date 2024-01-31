import React from "react";
import * as yup from "yup";
import { Form, TextField } from "../components/forms";

const validationSchema = yup.object().shape({
    username: yup.string().required("Username is required"),
});

const TextFieldWithForm = (textFieldProps) => (
    <Form validationSchema={validationSchema} initialValues={{ username: "" }}>
        <TextField name="username" {...textFieldProps} />
    </Form>
);

export default {
    title: "Forms/TextField",
    component: TextFieldWithForm,
    // More on argTypes: https://storybook.js.org/docs/react/api/argtypes
    parameters: {
        docs: {
            description: {
                component: "Textfield component with Formik integrations",
            },
        },
    },
    argTypes: {
        name: {
            type: "string",
            description: "Field name to be referenced by Formik",
            control: { disable: true },
            table: {
                type: {
                    summary: "string",
                },
            },
        },
        label: {
            type: "string",
            description: "Title for the text field",
            control: { type: "text" },
            table: {
                type: {
                    summary: "string",
                },
            },
        },
        placeholder: {
            type: "string",
            description: "Helps to give user an idea about what to input",
            control: { type: "text" },
            table: {
                type: {
                    summary: "string",
                },
            },
        },
        type: {
            type: "string",
            defaultValue: "text",
            description: "Type of input",
            control: { type: "radio" },
            options: ["text", "email", "number", "password"],
            table: {
                type: {
                    summary: "string",
                    detail: "text | email | number | password",
                },
            },
        },
        disabled: {
            control: "boolean",
            defaultValue: true,
            description:
                "Remove ability of editing and make the field view only",
            table: {
                type: {
                    summary: "boolean",
                },
            },
        },
    },
};

// More on component templates: https://storybook.js.org/docs/react/writing-stories/introduction#using-args
const Template = (args) => <TextFieldWithForm {...args} />;

export const Default = Template.bind({});
// More on args: https://storybook.js.org/docs/react/writing-stories/args
Default.args = {
    name: "username",
    label: "Username",
    placeholder: "Field Placeholder",
    type: "text",
    disabled: false,
};
