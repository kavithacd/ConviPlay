mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"kavithacd@iima.ac.in\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\