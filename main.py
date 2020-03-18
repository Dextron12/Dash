# DARK DRAGONS LANUCHER FOR ALL GAMES AND PROGRAMS MADE BY DARKS DRAGONS
# CREATED BY DEXTRON12
# ----------------------------------------------------------------------
# - ERROR (CODE HAS SERIOUS PROBLEMS MUST FIX - DETAILED PROBLEMS ATTACHED TO MESSSAGE)

import pygame
import math
import sqlite3

bg = (50, 50, 50)
pygame.init()

settings = {'displayMode': 'Dark'}

class Apps:

    Toolbars = ['Home','Profile','Library','Friends']

    def Home(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.VIDEORESIZE:
                    Greeter.window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    Greeter.width, Greeter.height = event.w, event.h
            Greeter.window.fill(bg)

            #GUI.Toolbar(GUI, 0,0,236,30,(105,105,105), (70,102, 255), (22, 100, 8), self.Toolbars, Greeter.window, 0)
            for iterTools in range(len(self.Toolbars)):
                GUI.Toolbar(GUI, iterTools*236, 0, 236,30, (105, 105, 105), (70, 102, 255), (22, 100, 8), self.Toolbars, Greeter.window, iterTools, self.Toolbars[iterTools])

            pygame.display.flip()

    def Profile(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.VIDEORESIZE:
                    Greeter.window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    Greeter.width, Greeter.height = event.w, event.height
            Greeter.window.fill(bg)
            for iterTools in range(len(self.Toolbars)):
                GUI.Toolbar(GUI, iterTools*236, 0, 236,30, (105, 105, 105), (70, 102, 255), (22, 100, 8), self.Toolbars, Greeter.window, iterTools, self.Toolbars[iterTools])

            pygame.display.flip()

    def Library(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.VIDEORESIZE:
                    Greeter.window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    Greeter.width, Greeter.height = event.w, event.h
            Greeter.window.fill(bg)
            for iterTools in range(len(self.Toolbars)):
                GUI.Toolbar(GUI, iterTools*236, 0, 236,30, (105, 105, 105), (70, 102, 255), (22, 100, 8), self.Toolbars, Greeter.window, iterTools, self.Toolbars[iterTools])

            pygame.display.flip()

    def Friends(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.VIDEORESIZE:
                    Greeter.window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    Greeter.width, Greeter.height
            Greeter.window.fill(bg)
            for iterTools in range(len(self.Toolbars)):
                GUI.Toolbar(GUI, iterTools*236, 0, 236,30, (105, 105, 105), (70, 102, 255), (22, 100, 8), self.Toolbars, Greeter.window, iterTools, self.Toolbars[iterTools])

            pygame.display.flip()


class GUI:

    def text(x,y,color, font, size, msg, surf):
        font = pygame.font.SysFont(font, int(size))
        text = font.render(msg, False, color)
        textRect = text.get_rect()
        textRect.center = (x,y)
        surf.blit(text, textRect)

    def textButton(self, x,y, ic, ac, font, size, msg, surf, func=None, funcArgs=None):
        mouse,click = pygame.mouse.get_pos(), pygame.mouse.get_pressed()
        if x+size > mouse[0]> x and y+size > mouse[1] > y:
            self.text(x,y,ac,font,size,msg,surf)
            if click[0] == 1:
                func(funcArgs)
        else:
            self.text(x,y,ic,font, size, msg, surf)



    def form(self,surf, formData, x, y, w, h, typing, formInUse, hideInput=False, mode=settings.get('displayMode')):
        if mode == 'Dark':
            pygame.draw.rect(surf, (255, 255, 255), (x,y,w,h))
            if typing == False and formData.get(formInUse) == '': # IF FORM IS EMPTY
                self.text(x+(w/2), y+(h/2), (47, 79, 79), 'Arial', 15, formData[formInUse], surf)
                self.text(x+(w/2), y+(h/2), (105, 105, 105), 'Arial', 15, formInUse, surf)
            elif typing == False and formData.get(formInUse) != '': # FORM HAS USER DATA. DISPLAY IT WHEN NOT TYPYNG
                if hideInput != False:
                    self.text(x+(w/2), y+(h/2), (47, 79, 79), 'Arial', 15, '*'*len(formData.get(formInUse)), surf)
                else:
                    self.text(x+(w/2), y+(h/2), (47, 79, 79), 'Arial', 15, formData.get(formInUse), surf)
            elif typing == True and formData.get(formInUse): # FORM HAS DATA WHILE YOUR TYPING
                if hideInput != False:
                    self.text(x+(w/2), y+(h/2), (0,0,0), 'Arial', 15, '*'*len(formData.get(formInUse)), surf)
                else:
                    self.text(x+(w/2), y+(h/2), (0,0,0), 'Arial', 15, formData.get(formInUse), surf)
        else: # LIGHT MODE
            pygame.draw.rect(surf, (47, 79, 79), (x,y,w,h))

        mouse,click = pygame.mouse.get_pos(), pygame.mouse.get_pressed()
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            if click[0] == 1:
                typing = True
        return typing, formData

    def Toolbar(self, x,y,w,h,bgColor, ac, ic, toolbars, surf, toolIter, func=None):
        mouse,click = pygame.mouse.get_pos(), pygame.mouse.get_pressed()
        
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(surf, bgColor, (x,y,w,h))
            pygame.draw.rect(surf, ac, (x,(y+h)-5,w,5)) # ACTIVE LINE
            if click[0] == 1 and func != None:
                getattr(Apps, func)(Apps)
        else:
            pygame.draw.rect(surf, bgColor, (x,y,w,h)) # BG
            pygame.draw.rect(surf, ic, (x,(y+h)-5,w,5)) # LINE
        self.text(x+(w/2), y+(h/2), (0,0,0), 'Arial', h/2, toolbars[toolIter], surf)
        






        
            


class Greeter:
    width,height = 1024, 700
    window = pygame.display.set_mode((width,height), pygame.RESIZABLE)
    err = None

    def Login(self):
        forms = {'Username': '', 'Password': ''}
        typing, typing1 = False, False
        formID = 0 # grabs first from and works on forms in order
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.VIDEORESIZE:
                    self.window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    self.width, self.height = event.w, event.h
                if event.type == pygame.KEYDOWN:
                    #event.unicode
                    if typing == True or typing1 == True:
                        if event.key == pygame.K_BACKSPACE:
                            if len(forms.get('Username')) > 0:
                                forms[list(forms)[formID]] = forms['Username'].strip(forms['Username'][-1])
                        elif event.key == pygame.K_RETURN: # FORM IS COMPLETED BY USER MOVE TO NEXT FORM.
                            if formID+1 < len(forms): # CHECKS IF THERE ARE ANY MORE FORMS IF NOT DONT ADD ANOTHER FORM ID
                                formID += 1
                            else:
                                formID = -1 # SETS FORM ID TO LOCK LAST FORM *** note *** this doesnt work! form must lock perferbly to submit
                                typing, typing1 = False, False
                        else:
                            forms[list(forms)[formID]] += event.unicode
                        

            self.window.fill(bg)
            GUI.text(self.width/2, 20, (22, 100, 8), 'Arial', 35, 'Login', self.window)

            typing, forms = GUI.form(GUI, self.window, forms, 100, 150, self.width-200, 30, typing, 'Username')
            typing1, forms = GUI.form(GUI, self.window, forms, 100, 190, self.width-200, 30, typing1, 'Password', True)

            pygame.draw.rect(self.window, (22, 100, 8), (0,self.height-30,self.width,30))

            GUI.textButton(GUI, self.width-120, 240, (22, 100, 8), (70, 102, 255), 'Arial', 20, 'Login', self.window, Greeter.authenticate, [Greeter, forms.get('Username'), forms.get('Password')])
            GUI.textButton(GUI, 100, 240, (22, 100, 8), (70, 102, 255), 'Arial', 20, 'New Account', self.window, Greeter.newUser, Greeter)


            pygame.display.flip()

            if formID == 1:
                typing, typing1 = False, True

            if self.err != None:
                if self.err == False: # USER AS PASSED AUTHENTICATION
                    Apps.Home(Apps)
                else:
                    GUI.text(self.width-120, 80, (255,0,0), 'Arial', 15, 'Failed to authenticate username: %s' % forms.get('Username'), self.window)

    def authenticate(args):
        self, username, password = args[0], args[1], args[2]
        if username == 'Dextron12':
            if password == 'ethan333':
                self.err = False
        else: # USER HAS FAILED AUTHENTICATION TEST
            self.err = True

    def newUser(self):
        forms = {'Username': '', 'Firstname': '', 'Lastname': '', 'Password': '', 'Email': ''}
        typing = False
        focusForm = 'Username'
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.VIDEORESIZE:
                    self.window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    self.width, self.height = event.w, event.h
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if len(forms[focusForm]) > 0:
                            forms[focusForm] = forms[focusForm].strip(forms[focusForm][-1])
                    else:
                        forms[focusForm] += event.unicode
            self.window.fill(bg)

            typing, forms = GUI.form(GUI, self.window, forms, 100, 150, self.width-200, 30, typing, 'Username')

            pygame.display.flip()


                    
        


Greeter.Login(Greeter)
#Apps.Home(Apps)
