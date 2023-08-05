class NodeTree:
    pass


class ClassToken(NodeTree):
    def __init__(self, instance, chidren) -> None:
        super().__init__()
        self.instance = instance
        self.children = chidren


class DuplicatedInstance(NodeTree):
    def __init__(self, nameInstance):
        self.nameInstance = nameInstance


class Attribute(NodeTree):
    def __init__(self, value: str, children):
        self.value: str = value
        self.children = children


class FileGenerator:
    def createAST(self, objectToAnalyze, listDuplicatedObject):
        def errorEncountered(element):
            raise Exception("Dictionnary not supported")

        def createChildrenAST(listElement):
            listToken = []
            for elem in listElement:
                listToken.append(self.createAST(elem, listDuplicatedObject))
            return listToken

        switcher = {
          int: lambda element: element,
          float: lambda element: element,
          list: lambda element: createChildrenAST(element),
          dict: errorEncountered,
          str: lambda element: element,
        }
        if objectToAnalyze.__class__ in switcher:
            return switcher[objectToAnalyze.__class__](objectToAnalyze)
        else:
            listChildren = []
            attributes = objectToAnalyze.__dict__.keys()
            for attribute in attributes:
                childAST = self.createAST(objectToAnalyze.__dict__[attribute], listDuplicatedObject)
                if childAST != [] and childAST != None:
                    listChildren.append(Attribute(attribute, childAST))
            return ClassToken(objectToAnalyze, listChildren)

    def createStringFromAST(self, pythonObject) -> str:
        def createStringForInstance(instance: ClassToken) -> str:
            stringRepr = instance.instance.__class__.__name__ + "("
            for attribute in instance.children:
                stringRepr += self.createStringFromAST(attribute) + ","
            return stringRepr + ")"

        def createStringForNumeric(instance) -> str:
            return instance

        def createStringForString(instance) -> str:
            return "\"" + instance + "\""

        def createStringForList(listInstance) -> str:
            stringRepr = "["
            for elem in listInstance:
                stringRepr += self.createStringFromAST(elem) + ","
            return stringRepr + "]"

        def createStringForAttribute(attribute: Attribute) -> str:
            stringRepr = attribute.value + "=" + \
                self.createStringFromAST(attribute.children)
            return stringRepr

        def createStringForDuplicated(duplicatedInstance, bloc):
            return duplicatedInstance.nameInstance

        switcher = {
          int: createStringForNumeric,
          float: createStringForNumeric,
          list: createStringForList,
          str: createStringForString,
          DuplicatedInstance: createStringForDuplicated,
          Attribute: createStringForAttribute,
        }
        if pythonObject.__class__ in switcher:
            return switcher[pythonObject.__class__](pythonObject)
        else:
            return createStringForInstance(pythonObject)

    def generatePyFileFromUrdf2Model(self, model, pyFilePath):
        ast = self.createAST(model, {})
        pythonFile = self.createStringFromAST(ast)
        with open(pyFilePath, "w") as f:
            f.write(pythonFile)
