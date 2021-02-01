
#include <Python.h>

#include <iostream>
#include <string>

static PyObject *
printString(PyObject * self, PyObject* args)
{
    const char * toPrint;
    if(!PyArg_ParseTuple(args, "s", &toPrint))
    {
        return NULL;
    }
    std::cout << toPrint << std::endl;
    Py_RETURN_NONE;
}

static PyMethodDef EmbMethods[] = {
        {"printMessage", printString, METH_VARARGS, "Return the string recieved from websocket server"},
        {NULL, NULL, 0, NULL}
};

static struct PyModuleDef pyex = {
        PyModuleDef_HEAD_INIT,
        "pyex",
        "",
        -1,
        EmbMethods
};


PyMODINIT_FUNC PyInit_pyex() {
    return PyModule_Create(&pyex);
}