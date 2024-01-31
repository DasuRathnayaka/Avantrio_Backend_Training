import React from "react";

const DefaultTypography = ({ variant = "", text = "Typography" }) => (
    <p className={variant}>{text}</p>
);

// More on default export: https://storybook.js.org/docs/react/writing-stories/introduction#default-export
export default {
    title: "Typography",
    component: DefaultTypography,
    // More on argTypes: https://storybook.js.org/docs/react/api/argtypes
    parameters: {
        docs: {
            description: {
                component: "Temporary preview of available typography styling",
            },
        },
    },
    argTypes: {
        variant: {
            type: "string",
            defaultValue: "",
            description:
                "Variations from all available typography styles in bootstrap",
            control: { type: "radio" },
            options: ["", "h1", "h2", "h3", "h4", "h5", "h6"],
            table: {
                type: {
                    summary: "string",
                    detail: "h1 | h2 | h3 | h4 | h5 | h6",
                },
            },
        },
        text: {
            type: "string",
            description: "Preview text.",
            control: { type: "text" },
            table: {
                type: {
                    summary: "string",
                },
            },
        },
    },
};

// More on component templates: https://storybook.js.org/docs/react/writing-stories/introduction#using-args
const Template = (args) => <DefaultTypography {...args} />;

export const Default = Template.bind({});
// More on args: https://storybook.js.org/docs/react/writing-stories/args
Default.args = {
    text: "Default Text",
};

export const Heading1 = Template.bind({});
Heading1.args = {
    variant: "h1",
    text: "Heading 1",
};

export const Heading2 = Template.bind({});
Heading2.args = {
    variant: "h2",
    text: "Heading 2",
};

export const Heading3 = Template.bind({});
Heading3.args = {
    variant: "h3",
    text: "Heading 3",
};

export const Heading4 = Template.bind({});
Heading4.args = {
    variant: "h4",
    text: "Heading 4",
};

export const Heading5 = Template.bind({});
Heading5.args = {
    variant: "h5",
    text: "Heading 5",
};

export const Heading6 = Template.bind({});
Heading6.args = {
    variant: "h6",
    text: "Heading 6",
};
