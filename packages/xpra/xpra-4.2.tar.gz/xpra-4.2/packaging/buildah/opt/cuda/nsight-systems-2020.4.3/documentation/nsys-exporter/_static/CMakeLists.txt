set(DOCS_LOCATION "${CMAKE_CURRENT_SOURCE_DIR}")

set(DOCS_OUTPUT "${CMAKE_CURRENT_BINARY_DIR}/nsys-exporter_docs.tar.gz")
set(DOCS_BUILDDIR "${CMAKE_CURRENT_BINARY_DIR}/docsbuild")
set(DOCS_PICKLES "${CMAKE_CURRENT_BINARY_DIR}/pickles")


set(DOCS
    "conf.py"
    "custom.css"
    "examples.rst"
    "exported_data.rst"
    "index.rst"
    "json_text_format.rst"
    "overview.rst"
    "composite.report32.results.txt"
    "composite.report32.sql"
    "cuda_kernel_api.report32.sql"
    "cuda_kernel_api.report32.results.txt"
    "cuda_bt.report705.sql"
    "cuda_bt.report705.results.txt"
    "fecs.gpuctxsw.sql"
    "fecs.gpuctxsw.results.txt"
    "fps_histogram.dx12.sql"
    "fps_histogram.dx12.results.txt"
    "func_table.report32.sql"
    "func_table.report32.results.txt"
    "map.cunvtx.sql"
    "map.cunvtx.results.txt"
    "osrt.report32.sql"
    "osrt.report32.results.txt"
    "overhead.report32.sql"
    "overhead.report32.results.txt"
    "sched.report32.sql"
    "sched.report32.results.txt"
    "sli.report109.sql"
    "sli.report109.results.txt"
    "streams.report32.sql"
    "streams.report32.results.txt"
    "syscall_histogram.ftrace.sql"
    "syscall_histogram.ftrace.results.txt"
    "extract_jsonl.ftrace.sql"
    "extract_jsonl.ftrace.results.txt"
    "origin.simpleCudaGraphs.sql"
    "origin.simpleCudaGraphs.results.txt"
    # "h5dump -H" results - currently as tests only.
    "stub.cunvtx.h5dump"
    "stub.dx12.h5dump"
    "stub.gpuctxsw.h5dump"
    "stub.report32.h5dump"
    "stub.sli.h5dump"
    "stub.ftrace.h5dump"
)

add_custom_command(
    OUTPUT "${DOCS_OUTPUT}"
    COMMAND "${CMAKE_COMMAND}" -E remove "${DOCS_OUTPUT}"
    COMMAND "${CMAKE_COMMAND}" -E remove_directory "${DOCS_BUILDDIR}"
    COMMAND "${PYTHON3_CMD}" -m sphinx -b html -E -q -W -d "${DOCS_PICKLES}"
        "${DOCS_LOCATION}" "${DOCS_BUILDDIR}"
    COMMAND "${CMAKE_COMMAND}" -E tar zcf "${DOCS_OUTPUT}" "${DOCS_BUILDDIR}"
    DEPENDS "${DOCS}"
    COMMENT "Building 'nsys export' documentation."
    VERBATIM
)

add_custom_target(QdrepExporter_BuildDocsArchive DEPENDS "${DOCS_OUTPUT}")
set_property(TARGET QdrepExporter_BuildDocsArchive PROPERTY IMPORTED_LOCATION "${DOCS_OUTPUT}")

set(QdrepExporter_DOCS "${DOCS}" CACHE INTERNAL "")
set(QdrepExporter_DOCS_LOCATION "${DOCS_LOCATION}" CACHE INTERNAL "")

# The function QdrepExporter_AddDocsTests is used to defer actual definition
# until "nsys" aka quadd_d target is available.
# There's no indent to keep code readable, due to 80/100 line length limit.
function(QdrepExporter_AddDocsTests)

# Documentation examples testing.
get_property(QdrepExporter_Location TARGET quadd_d PROPERTY LOCATION)
AgoraGetDestinationPath(TEST_BIN "" QdrepExporter_TestsDir QdrepExporter_TestsSymDir)

get_property(LibExporter_Location TARGET ExporterLibrary PROPERTY LOCATION)
get_filename_component(LibExporter_Location "${LibExporter_Location}" DIRECTORY)

function(QdrepExporter_GenerateDocTests TEST_REPORT RESULTS)
    get_filename_component(REPORT_NAME "${TEST_REPORT}" NAME_WE)
    set(SQL_DATABASE "${CMAKE_CURRENT_BINARY_DIR}/${REPORT_NAME}.sqlite")

    add_custom_command(
        OUTPUT "${SQL_DATABASE}"
        COMMAND "${CMAKE_COMMAND}" -E remove "${SQL_DATABASE}"
        COMMAND "${CMAKE_COMMAND}" -E env
            LD_LIBRARY_PATH="${LibExporter_Location}:${QdrepExporter_TestsDir}"
            "${QdrepExporter_Location}" export --type sqlite
            --output "${SQL_DATABASE}" "${TEST_REPORT}"
        DEPENDS quadd_d ExporterLibrary "${TEST_REPORT}"
        COMMENT "Generating SQLite test database: ${REPORT_NAME}.sqlite"
    )

    foreach(DOC_FILE ${QdrepExporter_DOCS})
        if("${DOC_FILE}" MATCHES ".*[.]${REPORT_NAME}[.]sql$")
            get_filename_component(TESTCASE_NAME "${DOC_FILE}" NAME_WE)

            set(SQL_INPUT "${QdrepExporter_DOCS_LOCATION}/${DOC_FILE}")
            set(SQL_REFERENCE
                "${QdrepExporter_DOCS_LOCATION}/${TESTCASE_NAME}.${REPORT_NAME}.results.txt")
            set(SQL_OUTPUT
                "${CMAKE_CURRENT_BINARY_DIR}/${TESTCASE_NAME}.${REPORT_NAME}.results.new")
            set(SQL_TEMP_DATABASE
                "${SQL_DATABASE}_${TESTCASE_NAME}.sqlite")
            set(SQL_CHECK_RESULT
                "${CMAKE_CURRENT_BINARY_DIR}/${TESTCASE_NAME}.${REPORT_NAME}.sqlite.check")

            add_custom_command(
                OUTPUT "${SQL_OUTPUT}"
                COMMAND "${CMAKE_COMMAND}" -E copy_if_different
                    "${SQL_DATABASE}" "${SQL_TEMP_DATABASE}"
                COMMAND "${AGORA_SQLITE3_CMD}" -column -header -cmd ".output ${SQL_OUTPUT}"
                    "${SQL_TEMP_DATABASE}" ".read ${SQL_INPUT}"
                DEPENDS "${SQL_INPUT}" "${SQL_DATABASE}" "${AGORA_SQLITE3_CMD}"
                COMMENT "Generating 'nsys export' documentation part: '${SQL_OUTPUT}'."
                VERBATIM
            )

            add_custom_command(
                OUTPUT "${SQL_CHECK_RESULT}"
                COMMAND "${CMAKE_COMMAND}" -E compare_files
                    "${SQL_OUTPUT}" "${SQL_REFERENCE}"
                COMMAND "${CMAKE_COMMAND}" -E touch "${SQL_CHECK_RESULT}"
                DEPENDS "${SQL_INPUT}" "${SQL_OUTPUT}" "${SQL_REFERENCE}"
                COMMENT "Checking 'nsys export' documentation part: '${SQL_INPUT}'."
                VERBATIM
            )

            # If the test above fails, e.g:
            #
            # Checking 'nsys export' documentation part: '/home/akostikov/agora/QuadD/Tools/QdrepExporter/Docs/streams.sql'.
            # FAILED:
            # ...
            # Files "/home/.../Docs/streams.results.new" to
            # "/home/.../Docs/streams.results.txt" are different.
            #
            # This means that the new output from example queries is different.
            # After verifying that the new data makes sense, fix with:
            #
            # cat streams.sql | sqlite3 -column -header report32.sqlite > streams.results.txt
            #

            list(APPEND RESULTS "${SQL_CHECK_RESULT}")
        endif()
    endforeach(DOC_FILE ${QdrepExporter_DOCS})

    set(${RESULTS} ${${RESULTS}} PARENT_SCOPE)
endfunction()

function(QdrepExporter_GenerateHDFTests TEST_REPORT RESULTS)
    get_filename_component(REPORT_NAME "${TEST_REPORT}" NAME_WE)
    set(H5_DATABASE "${CMAKE_CURRENT_BINARY_DIR}/${REPORT_NAME}.h5")

    add_custom_command(
        OUTPUT "${H5_DATABASE}"
        COMMAND "${CMAKE_COMMAND}" -E remove "${H5_DATABASE}"
        COMMAND "${CMAKE_COMMAND}" -E env
            LD_LIBRARY_PATH="${LibExporter_Location}:${QdrepExporter_TestsDir}"
            "${QdrepExporter_Location}" export --type hdf
            --output "${H5_DATABASE}" "${TEST_REPORT}"
        DEPENDS quadd_d ExporterLibrary "${TEST_REPORT}"
        COMMENT "Generating HDF5 test database: ${REPORT_NAME}.h5"
    )

    foreach(DOC_FILE ${QdrepExporter_DOCS})
        if("${DOC_FILE}" MATCHES ".*[.]${REPORT_NAME}[.]h5dump$")
            get_filename_component(TESTCASE_NAME "${DOC_FILE}" NAME_WE)

            set(H5_REFERENCE "${QdrepExporter_DOCS_LOCATION}/${DOC_FILE}")
            set(H5_OUTPUT
                "${CMAKE_CURRENT_BINARY_DIR}/${TESTCASE_NAME}.${REPORT_NAME}.results.new")
            set(H5_CHECK_RESULT
                "${CMAKE_CURRENT_BINARY_DIR}/${TESTCASE_NAME}.${REPORT_NAME}.h5.check")

            # "--output=${H5_OUTPUT}" doesn't work for header info.

            # It's important to use relative path to .h5 file, since "h5dump -H"
            # includes the path in the first line of output.
            add_custom_command(
                OUTPUT "${H5_OUTPUT}"
                COMMAND "${AGORA_H5DUMP_CMD}" -H "${REPORT_NAME}.h5" > "${H5_OUTPUT}"
                WORKING_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}"
                DEPENDS "${H5_DATABASE}" "${AGORA_H5DUMP_CMD}"
                COMMENT "Generating 'nsys export' documentation part: '${H5_OUTPUT}'."
                VERBATIM
            )

            add_custom_command(
                OUTPUT "${H5_CHECK_RESULT}"
                COMMAND "${CMAKE_COMMAND}" -E compare_files
                    "${H5_OUTPUT}" "${H5_REFERENCE}"
                COMMAND "${CMAKE_COMMAND}" -E touch "${H5_CHECK_RESULT}"
                DEPENDS "${H5_REFERENCE}" "${H5_OUTPUT}"
                COMMENT "Checking 'nsys export' documentation part: '${H5_REFERENCE}'."
                VERBATIM
            )

            list(APPEND RESULTS "${H5_CHECK_RESULT}")
        endif()
    endforeach(DOC_FILE ${QdrepExporter_DOCS})

    set(${RESULTS} ${${RESULTS}} PARENT_SCOPE)
endfunction()


set(TEST_REPORTS
    "report32.qdrep"
    "dx12.qdrep"
    "gpuctxsw.qdrep"
    "cunvtx.qdrep"
    "report109.qdrep"
    "report705.qdrep"
    "ftrace.qdrep"
    "simpleCudaGraphs.qdrep"
)

set(SQL_CHECK_RESULTS)
set(HDF_CHECK_RESULTS)

foreach(REPORT_FILE ${TEST_REPORTS})
    set(CHECK_RESULTS)

    QdrepExporter_GenerateDocTests("${QdrepExporter_DOCS_LOCATION}/${REPORT_FILE}" CHECK_RESULTS)
    if(NOT CHECK_RESULTS)
        message(SEND_ERROR "No SQL example queries to check have been found.")
    endif()
    list(APPEND SQL_CHECK_RESULTS "${CHECK_RESULTS}")


    QdrepExporter_GenerateHDFTests("${QdrepExporter_DOCS_LOCATION}/${REPORT_FILE}" CHECK_RESULTS)
    if(NOT CHECK_RESULTS)
        message(SEND_ERROR "No HDF5 header info to check have been found.")
    endif()
    list(APPEND HDF_CHECK_RESULTS "${CHECK_RESULTS}")
endforeach()

add_custom_target(QdrepExporter_CheckDocs_SQL DEPENDS ${SQL_CHECK_RESULTS})
add_custom_target(QdrepExporter_CheckDocs_HDF DEPENDS
    QdrepExporter_CheckDocs_SQL ${HDF_CHECK_RESULTS})

add_dependencies(quadd QdrepExporter_CheckDocs_HDF)

endfunction(QdrepExporter_AddDocsTests)
