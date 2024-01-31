export const getRouteObj = (arr) => {
    let paths = {};
    const getRouteRouteId = (arr) => {
        for (let item of arr) {
            if (item.routeId) {
                paths[item.routeId] = item.routeId;
            }
            if (item.children) {
                getRouteRouteId(item.children);
            }
        }
        return paths;
    };

    return getRouteRouteId(arr);
};
