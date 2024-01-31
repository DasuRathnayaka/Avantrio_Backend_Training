import React from "react";
import {
    Checkbox,
    Form,
    Select,
    SubmitButton,
    TextField,
} from "../../components/forms";
import { useGetMyProfileQuery } from "../../services/userService";

export default function FormsExamplePage() {
    useGetMyProfileQuery();
    return (
        <div className="container mt-5">
            <div className="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
                <h1 className="h2">Forms Example</h1>
                <div className="btn-toolbar mb-2 mb-md-0">
                    <div className="btn-group me-2">
                        <button
                            type="button"
                            className="btn btn-sm btn-outline-secondary"
                        >
                            Share
                        </button>
                        <button
                            type="button"
                            className="btn btn-sm btn-outline-secondary"
                        >
                            Export
                        </button>
                    </div>
                    <button
                        type="button"
                        className="btn btn-sm btn-outline-secondary dropdown-toggle"
                    >
                        <span data-feather="calendar"></span>
                        This week
                    </button>
                </div>
            </div>

            <h2>User Registration Form</h2>
            <Form initialValues={{}}>
                <div className="row pt-2">
                    <div className="col-3">
                        <TextField name="first_name" label="First Name" />
                    </div>
                    <div className="col-3">
                        <TextField name="last_name" label="Last Name" />
                    </div>
                </div>
                <div className="row pt-2">
                    <div className="col-3">
                        <Select
                            name="gender"
                            label="Gender"
                            options={[
                                { label: "Male", value: 0 },
                                { label: "Female", value: 1 },
                                { label: "Other", value: 2 },
                            ]}
                        />
                    </div>
                </div>
                <div className="row pt-4">
                    <div className="col-3">
                        <Checkbox
                            name="agree"
                            label="I Agreee to Terms and Conditions"
                        />
                    </div>
                </div>
                <div className="row pt-2">
                    <div className="col-3">
                        <SubmitButton />
                    </div>
                </div>
            </Form>
        </div>
    );
}
