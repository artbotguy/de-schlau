https://docs.google.com/document/d/1TVrircHD2WZEGAsbt9NMoaL-W96CkGxA7JVhFFT4nSQ/edit?tab=t.0

DeSchlau

При первом запуске (если миграции не были включены и т.п.):
    1. Может понадобится выполнять (и далее что прописано в соотв. ошибке):
        docker-compose exec web flask db init
    


ALL_ERRORS
    docker
        ERR: 
            error getting credentials - err: exec: "docker-credential-desktop": executable file not found in $PATH, out: ``
        SOL: 
            rm ~/.docker/config.json
