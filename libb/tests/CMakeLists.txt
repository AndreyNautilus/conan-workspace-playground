set(TEST_TARGET "${PROJECT_NAME}-unittests")

add_executable(${TEST_TARGET}
  libb_test.cpp
)

target_link_libraries(${TEST_TARGET}
  PRIVATE
    ${PROJECT_NAME}
)

add_test(
  NAME ${TEST_TARGET}
  COMMAND ${TEST_TARGET}
  WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
)
