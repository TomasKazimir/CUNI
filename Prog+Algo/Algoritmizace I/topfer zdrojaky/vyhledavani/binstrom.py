class Vrchol:
    """vrchol binárního stromu"""
    
    def __init__(self, x = None):
        self.info = x             # uložená hodnota
        self.levy = None          # levý syn
        self.pravy = None         # pravý syn

    def preorder(self):
        """
          průchod stromem s kořenem v tomto vrcholu
          metodou preorder, vypisuje hodnoty všech vrcholů
        """
        print(self.info)
        if self.levy != None:
            self.levy.preorder()
        if self.pravy != None:
            self.pravy.preorder()

    def inorder(self):
        """
          průchod stromem s kořenem v tomto vrcholu
          metodou inorder, vypisuje hodnoty všech vrcholů
        """
        if self.levy != None:
            self.levy.inorder()
        print(self.info)
        if self.pravy != None:
            self.pravy.inorder()

    def postorder(self):
        """
          průchod stromem s kořenem v tomto vrcholu
          metodou postorder, vypisuje hodnoty všech vrcholů
        """
        if self.levy != None:
            self.levy.postorder()
        if self.pravy != None:
            self.pravy.postorder()
        print(self.info)
