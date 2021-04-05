# Lancement de ZAP...
# Attente du lancement de Zap...
# Lancement d'une session...
# Création d'un nouveau contexte...
# Ajout des URL du contexte...
# Ajout des URL hors contexte...
# Choisir la gestion de session (sessionManagement) "cookieBasedSessionManagement" pour cookie, "httpAuthSessionManagement" pour JWT
zap.sessionManagement.set_session_management_method(
                contextid=contextId, methodname=sessionManagement,
                methodconfigparams=None))
# Zap en mode attaque...
# Chargement et lancement du script clearGlobalVariables.py
zap.script.load(scriptname='clearGlobalVariables.py', scripttype='standalone',
                scriptengine='jython',
                filename='./clearGlobalVariables.py',
                scriptdescription='Description du script'))
zap.script.run_stand_alone_script(scriptname='clearGlobalVariables.py')

# Chargement et activation du script doLogin.py
zap.script.load(scriptname='doLogin.py', scripttype='httpsender',
                scriptengine='jython',
                filename='./doLogin.py',
                scriptdescription='Description du script'))
zap.script.enable(scriptname='clearGlobalVariables.py')
# Authentification manuelle
zap.authentication.set_authentication_method(contextid=contextId,
                                           authmethodname='manualAuthentication',
                                           authmethodconfigparams=authParams))
# Scan passif via traditionnakl spider pour site en HTML
#   et via Ajax spider pour des applis avec beaucoup de javascript
# Scan actif
# Affichage des alertes de vulnérabilités trouvés