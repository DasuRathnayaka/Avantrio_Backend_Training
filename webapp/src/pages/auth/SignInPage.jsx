import { useNavigate } from "react-router-dom";
import { useSignInMutation } from "../../services/authService";
import {
    Form,
    SubmitButton,
    TextField,
    Checkbox,
} from "../../components/forms";
import { ACCESS_TOKEN_NAME, REFRESH_TOKEN_NAME } from "../../constants";

// TODO: remove inline styles
export default function SignInPage() {
    const navigate = useNavigate();
    const [signIn] = useSignInMutation();

    const handleSignInSubmit = async ({ username, password, remember }) => {
        const signInRes = await signIn({ username, password });
        if (signInRes.data) {
            // request succeeded
            if (signInRes.data.data?.access || signInRes.data.data?.refresh) {
                sessionStorage.setItem(
                    ACCESS_TOKEN_NAME,
                    signInRes.data.data?.access,
                );
                if (remember) {
                    localStorage.setItem(
                        REFRESH_TOKEN_NAME,
                        signInRes.data.data?.refresh,
                    );
                } else {
                    sessionStorage.setItem(
                        REFRESH_TOKEN_NAME,
                        signInRes.data.data?.refresh,
                    );
                }
                navigate("/app/tables");
            }
        }
        if (signInRes.error) {
            //request failed
        }
    };

    return (
        <div
            className="w-100 d-flex justify-content"
            style={{ height: "100vh" }}
        >
            <div className="w-100 m-auto p-2" style={{ maxWidth: 335 }}>
                <Form
                    initialValues={{
                        username: "",
                        password: "",
                        remember: false,
                    }}
                    onSubmit={handleSignInSubmit}
                >
                    <div className="d-flex flex-column align-items-center">
                        <img
                            className="mb-4"
                            src="/images/favicon.png"
                            alt=""
                            width="72"
                            height="57"
                        />
                        <h1 className="h3 mb-3 fw-normal">Please sign in</h1>
                        <TextField name="username" label="Email address" />

                        <div className="w-100 mt-3">
                            <TextField
                                name="password"
                                label="Password"
                                type="password"
                            />
                        </div>

                        <div className="checkbox my-3">
                            <Checkbox name="remember" label="Remember me" />
                        </div>
                        <SubmitButton variant={"outlined"}>
                            Sign In
                        </SubmitButton>
                        <p className="mt-5 mb-3 text-muted">&copy; 2017–2022</p>
                    </div>
                </Form>
            </div>
        </div>
    );
}
