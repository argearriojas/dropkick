execute_process(
    COMMAND python3 -c "import versioneer; print(versioneer.get_version())"
    OUTPUT_VARIABLE PACKAGE_VERSION
    OUTPUT_STRIP_TRAILING_WHITESPACE
)

message(STATUS "Package version: ${PACKAGE_VERSION}")

cmake_minimum_required(VERSION 3.15)
project(dropkick Fortran)

# Find Python and NumPy
find_package(Python REQUIRED COMPONENTS Interpreter Development.Module NumPy)

# Set Fortran flags
if(CMAKE_Fortran_COMPILER_ID MATCHES "GNU")
    set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -ffixed-form -fdefault-real-8")
endif()

# Platform specific settings
if(APPLE)
    execute_process(
        COMMAND gfortran -print-file-name=libgfortran.3.dylib
        OUTPUT_VARIABLE GFORTRAN_LIB
        OUTPUT_STRIP_TRAILING_WHITESPACE
    )
    execute_process(
        COMMAND gfortran -print-file-name=libquadmath.0.dylib
        OUTPUT_VARIABLE QUADMATH_LIB
        OUTPUT_STRIP_TRAILING_WHITESPACE
    )
    get_filename_component(GFORTRAN_DIR ${GFORTRAN_LIB} DIRECTORY)
    get_filename_component(QUADMATH_DIR ${QUADMATH_LIB} DIRECTORY)
    
    set(CMAKE_INSTALL_RPATH "${GFORTRAN_DIR};${QUADMATH_DIR}")
endif()

# Add the Fortran extension
python_add_library(_glmnet MODULE WITH_SOABI
    dropkick/_glmnet.pyf
    dropkick/src/glmnet/glmnet5.f90
)

# Link against Python
target_link_libraries(_glmnet PRIVATE Python::Module)
install(TARGETS _glmnet DESTINATION dropkick)

