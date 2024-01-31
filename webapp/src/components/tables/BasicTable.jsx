import React, { useMemo } from "react";
import { usePagination, useSortBy, useTable } from "react-table";

/**
 * Table component wrapped around `react-table`.
 * @param {{
 * data: any[],
 * columns: any[],
 * isSortable?: boolean,
 * isPaginated?: boolean,
 * pageSize?: boolean,
 * pageIndex?: number,
 * }} props
 * @returns {React.FunctionComponent}
 */
export default function BasicTable({
    data,
    columns,
    isSortable = false,
    isPaginated = false,
    pageSize = 10,
    currentPage = 0,
}) {
    const tableColumns = useMemo(
        () =>
            columns.map((col) => ({
                ...col,
                Header: col.header,
            })),
        [columns],
    );

    const pluginList = useMemo(() => {
        let list = [];

        if (isSortable) {
            list.push(useSortBy);
        }

        if (isPaginated) {
            list.push(usePagination);
        }

        return list;
    }, [isSortable, isPaginated]);

    const tableInstance = useTable(
        {
            columns: tableColumns,
            data: data,
            initialState: {
                pageSize: pageSize,
                pageIndex: currentPage,
            },
        },
        ...pluginList,
    );

    const getHeaderProps = (tableInstance, column) => {
        if (isSortable) {
            return column.getHeaderProps(column.getSortByToggleProps());
        }

        return column.getHeaderProps();
    };

    const { getTableProps, getTableBodyProps, headerGroups, rows, prepareRow } =
        tableInstance;

    return (
        <div className="table-responsive">
            <table className="table table-hover table-sm" {...getTableProps()}>
                <thead>
                    {headerGroups.map((headerGroup) => (
                        <tr {...headerGroup.getHeaderGroupProps()}>
                            {headerGroup.headers.map((column) => (
                                <th {...getHeaderProps(tableInstance, column)}>
                                    {column.render("Header")}
                                    {isSortable && (
                                        <span>
                                            {column.isSorted
                                                ? column.isSortedDesc
                                                    ? " 🔽"
                                                    : " 🔼"
                                                : ""}
                                        </span>
                                    )}
                                </th>
                            ))}
                        </tr>
                    ))}
                </thead>
                <tbody {...getTableBodyProps()}>
                    {(isPaginated ? tableInstance.page : rows).map((row) => {
                        prepareRow(row);
                        return (
                            <tr {...row.getRowProps()}>
                                {row.cells.map((cell) => {
                                    return (
                                        <td {...cell.getCellProps()}>
                                            {cell.render("Cell")}
                                        </td>
                                    );
                                })}
                            </tr>
                        );
                    })}
                </tbody>
            </table>

            {isPaginated && (
                <div className="table-pagination">
                    <nav>
                        <ul class="pagination">
                            <li
                                class={`page-item ${
                                    !tableInstance.canPreviousPage
                                        ? "disabled"
                                        : ""
                                }`}
                            >
                                <a
                                    className="page-link"
                                    href="#"
                                    onClick={tableInstance.previousPage}
                                >
                                    Previous
                                </a>
                            </li>
                            {[...Array(tableInstance.pageCount)].map((_, p) => (
                                <li
                                    class={`page-item ${
                                        p === tableInstance.state.pageIndex
                                            ? "active"
                                            : ""
                                    }`}
                                >
                                    <a
                                        className="page-link"
                                        href="#"
                                        onClick={() =>
                                            tableInstance.gotoPage(p)
                                        }
                                    >
                                        {p + 1}
                                    </a>
                                </li>
                            ))}
                            <li
                                class={`page-item ${
                                    !tableInstance.canNextPage ? "disabled" : ""
                                }`}
                            >
                                <a
                                    className="page-link"
                                    href="#"
                                    onClick={tableInstance.nextPage}
                                >
                                    Next
                                </a>
                            </li>
                        </ul>
                    </nav>
                </div>
            )}
        </div>
    );
}
