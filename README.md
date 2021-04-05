# DAST-owasp-zap-authentication-httpsender-oidc-oauth-kong
Tests dynamiques de sécurité (DAST) sous OWASP Zap avec authentification via JWT/bearer token (OpenID Connect/OAuth &amp; Kong)

Article complet sur :  
https://deeplylearning.fr/cybersecurite/tests-dynamiques-de-securite-dast-sous-owasp-zap-avec-authentification-via-jwt-bearer-token-openid-connect-oauth-kong/

## Structure
```
.
├── clearGlobalVariables.py           # script stand-alone 
├── doLogin.py                        # script httpSender
├── main.py                           # script global
├── utils.py                          # fonction diverses
└── dockerLaunch.py                   # tips pour lancer Zap via docker
```