import React from "react";

import Button from "../components/Button";

// More on default export: https://storybook.js.org/docs/react/writing-stories/introduction#default-export
export default {
    title: "Forms/Button",
    component: Button,
    // More on argTypes: https://storybook.js.org/docs/react/api/argtypes
    parameters: {
        docs: {
            description: {
                component:
                    "Native button wrapped to enable customization with bootstrap sizes and variants",
            },
        },
    },
    argTypes: {
        variant: {
            type: "string",
            defaultValue: "primary",
            description:
                "Supports all available variations in bootstrap buttons. Primary variation is selected by default",
            control: { type: "radio" },
            options: [
                "primary",
                "secondary",
                "outline-primary",
                "outline-secondary",
            ],
            table: {
                type: {
                    summary: "string",
                    detail: "primary | secondary | outline-primary | outline-secondary",
                },
            },
        },
        size: {
            type: "string",
            description: "Supports all available sizes in bootstrap buttons.",
            control: { type: "radio" },
            options: ["sm", "lg"],
            table: {
                type: {
                    summary: "string",
                },
            },
        },
        fullWidth: {
            control: "boolean",
            defaultValue: true,
            description: "If `true` button will take up full width",
            table: {
                type: {
                    summary: "boolean",
                },
            },
        },
        children: {
            description: "Label or child nodes",
            table: {
                type: {
                    summary: "JSX.Element",
                },
            },
        },
    },
};

// More on component templates: https://storybook.js.org/docs/react/writing-stories/introduction#using-args
const Template = (args) => <Button {...args} />;

export const Primary = Template.bind({});
// More on args: https://storybook.js.org/docs/react/writing-stories/args
Primary.args = {
    children: "Primary Variant",
};

export const Secondary = Template.bind({});
Secondary.args = {
    variant: "secondary",
    children: "Secondary Variant",
};

export const Outlined = Template.bind({});
Outlined.args = {
    variant: "outline-primary",
    children: "Outlined Variant",
};

export const Large = Template.bind({});
Large.args = {
    size: "lg",
    children: "Large Size",
};

export const Small = Template.bind({});
Small.args = {
    size: "sm",
    children: "Small Size",
};
