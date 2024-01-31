import React from "react";

const DefaultBoxShadow = ({ variant = "" }) => (
    <div className={`card text-center border-0 p-4 text-capitalize ${variant}`}>
        {variant}
    </div>
);

// More on default export: https://storybook.js.org/docs/react/writing-stories/introduction#default-export
export default {
    title: "Box Shadow",
    component: DefaultBoxShadow,
    // More on argTypes: https://storybook.js.org/docs/react/api/argtypes
    parameters: {
        docs: {
            description: {
                component: "Temporary preview of available box-shadow styling",
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
            options: ["shadow-sm", "shadow", "shadow-lg"],
            table: {
                type: {
                    summary: "string",
                    detail: "shadow-sm | shadow | shadow-lg",
                },
            },
        },
    },
};

// More on component templates: https://storybook.js.org/docs/react/writing-stories/introduction#using-args
const Template = (args) => <DefaultBoxShadow {...args} />;

export const Small = Template.bind({});
// More on args: https://storybook.js.org/docs/react/writing-stories/args
Small.args = {
    variant: "shadow-sm",
};

export const Medium = Template.bind({});
Medium.args = {
    variant: "shadow",
};

export const Large = Template.bind({});
Large.args = {
    variant: "shadow-lg",
};
