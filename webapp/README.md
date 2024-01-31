# React boilerplate

## Setting Up

### Setting up pre commit hooks

This repo uses pre-commit hooks to validate cording best practices. Follow the below steps to ensure the proper functinality of pre-commit hooks. Note that this is a one time operation.

1. `pip install pre-commit` (You can validate the installation by running `pre-commit --version`)
2. `pre-commit install` (This will install the required hook realted dependancies)

### Running dev server

This project requires node v14 hor higher.

1. `npm install`
2. Change `.env.development` for local development config
3. Change `.env.sample` to `.env` in production.
4. `npm start`

### VS Code setup

Install below Extensions

-   ESLint
-   Prettier (set this as default formatter for js/jsx/scss files)

## Coding Practices

### General rules and guidelines(new)

-   Move the business logic to hooks
-   Function naming conventions(tbd)
    -   function name should always start with a verb.
    -   event handle functions should start with the prefix "handle". eg: "handleClick"
-   Prop naming conventions
    -   props that expect handler functions should start with “on”. eg: “onSubmit”, “onClick”, “onUpdateSuccess”
    -   Props should be named relative to the context of the Component itself.(Find a good example for this.)
-   Component Naming convention
    -   Use nouns
    -   Be descriptive as much as possible. Lengthy names are okay
-   Develop reusable components in isolation using storybook.
-   Styles applied to a component shouldn’t affect anything outside the component itself.

### React/Javascript basics

-   Use functional components and hooks.
-   Minimise the usage of Context API.
-   useEffect is for side effects.
-   Derived values shoul be calculated while redering.(This makes code simple and maintanable. useMemo can be used to optimise this but not required in the early development iterations)
-   Use async/await. Avoid callbacks.

### Redux basics

-   Following things should go in redux store.
    1. State associated with business logic of the app.
    2. App wide UI state
-   Business logic should go in reducers. (avoid having logic in components and actions as much as possible).
-   Use `useSelector` hook to read data from redux state. Access relevant state from the lowest possible component in the component tree(i.e:Avoid prop drilling).
-   Refer to <a href="https://redux.js.org/style-guide" >redux style guide</a> for detailed guidelines.
-   Use <a href="https://redux-toolkit.js.org/">redux toolkit</a> to create actions and reducers.(store is already confugred for toolkit).
-   Insall redux dev tools extenstion in browser. Store is already configure to suppport dev tools.

### Data fetching

-   Two methods
    -   RTK-Query - Primary method
    -   Axios - for special cases like file upload
-   RTK-Query
    -   A service is defined to featch and store data in redux store.
    -   Data is cached by by rtk-query. We can definde cahce invalidation logic in the service.
    -   Loading/Error states are fully handled by rtk-query for each API endpoint.
-   Axios
    -   One api handler
    -   Inceptors
        -   To inject authorization header
        -   To check authorization failures and logout
    -   BASE URL should be defined in .env
    -   All API calls should be async
    -   ONLY use async await

### Routing

-   <a href="https://reactrouter.com/web/guides/quick-start">React router</a> handles routing.
-   `./routes` folder contains all the top level routing logic.
-   Declare all the routes inside (constansts/routes.js) file.
-   Use `useGetRoute` custom hook to navigate from route title (ex : useGetRoute("Home")).
-   `./routes/CustomRoutes` contains below custom route wrappers that helps in access control.
    -   RequireAuth - only logged in users can view
    -   PublicOnly - only logged out users can view (ex: Login, Register)
-   No wrapper component - anyone can view
-   Nested routing is preferred over state when rendering content inside a common layout(An app can have multiple levels of nesting).
-   Breadcrumbs should be connected to the router.
-   Use `useGetActivePath` custom hook to get the breadcrumbs
-   Modals/Tabs/Steppers inside pages should be connected to the router(use nested routing).
-   Use hooks provided by react-router.
    -   `useHistory` - gets the history object
    -   `useParams` - gets the route parameters
-   `history.push()` is preferred over `<Link/>`

### Form Submission

-   Use Fromik for handling forms.
-   Never use pure Formik components unless it’s absolutely necessary. Ping senior dev before doing that. Always use the wrappers from `components/FormElements`.
-   Create ThemedFormElements if your theming is significantly different from the base theme.
-   Use YUP schema validation.

### Tables

-   Use `components/paginatedTable` componets.
-   Pagination/Search should be connected to router.

## Loading placeholder animations

-   The new bootstrap version we are using in this boilerplate has [utility classes](https://getbootstrap.com/docs/5.2/components/placeholders/) for this
-   Use these bootstrap classes directly in your implementations.
-   Use these effectively to make sure that content won’t jump around in between loading and final state.

### Styling

-   Use scss.
-   Bootstrap 5 - use utility classes of Bootstrap as much as possible.
-   Create custom CSS classes only if necessary.
-   Implement the design system by overriding Bootstrap variables.
-   Declare all the variables in `variables.scss` file.
-   For each component have a seperate scss file.
-   To reuse the variables defined in the `variables.scss` file, use scss `@use` method. Example available in `sidebar.scss`

### Code formatting

-   1 tab or 4 spaces indentation
-   Functional component names - PascalCase
-   Variables, functions, hooks, routes - camelCase
-   Config contacts - BLOCK_CASE
-   Curly Braces should start on the same line
-   JSX file names - PascalCase, make them descriptive
-   Js file names (helpers, api, redux etc) - camelCase

## Directory structure

-   App.js - entrypoint
-   api.js - api endpoints handled by axios
-   State - redux related stuff
    -   reducers + actions = slices
    -   store
-   Service - api services defined by rtk-query.
-   Pages - page components
    -   One file per component.
-   Components - reusable components
    -   One file per component.
-   Utils - helper functions
-   routes/CustomRoutes - Routes discussed earlier
-   .env - environment config
-   hooks - custom hooks

## Documentation

-   Component documentation is done with the help of Storybook and JSDoc snippets in the component
    -   Complete React JSDoc reference is accessible [here](https://react-styleguidist.js.org/docs/documenting#using-jsdoc-tags)
