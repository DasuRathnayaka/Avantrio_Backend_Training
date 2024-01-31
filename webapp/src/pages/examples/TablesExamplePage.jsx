import React, { useMemo } from "react";
import { BasicTable } from "../../components/tables";

export default function DashboardPage() {
    return (
        <div className="container mt-5">
            <div className="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
                <h1 className="h2">Tables</h1>
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

            <h2>Section title</h2>
            <BasicTable
                data={[
                    {
                        name: "Manuj",
                        birthDate: "1994-11-26",
                        link: "http://google.com",
                        status: "Accepted",
                    },
                    {
                        name: "Manuj 2",
                        birthDate: "1994-11-26",
                        link: "http://google.com",
                        status: "Rejected",
                    },
                    {
                        name: "Manuj 3",
                        birthDate: "1994-11-26",
                        link: "http://google.com",
                        status: "Accepted",
                    },
                    {
                        name: "Manuj 4",
                        birthDate: "1994-11-26",
                        link: "http://google.com",
                        status: "Rejected",
                    },
                ]}
                columns={[
                    {
                        header: "Name",
                        accessor: "name",
                    },
                    {
                        header: "Birth Date",
                        accessor: (row) =>
                            new Date(row.birthDate).toDateString(),
                    },
                    {
                        header: "Status",
                        accessor: "status",
                        sortType: useMemo(() => {
                            return function (rowA, rowB, id) {
                                if (rowA.values[id] === "Accepted") {
                                    if (rowB.values[id] === "Accepted") {
                                        return 0;
                                    }

                                    return 1;
                                }
                                return -1;
                            };
                        }, []),
                    },
                    {
                        header: "View",
                        accessor: (row) => (
                            <a
                                className="btn btn-sm btn-outline-primary"
                                href={row.link}
                            >
                                View Profile
                            </a>
                        ),
                        disableSortBy: true,
                    },
                ]}
                isSortable={true}
                isPaginated={false}
                pageSize={2}
                currentPage={0}
            />
        </div>
    );
}
