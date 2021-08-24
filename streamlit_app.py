import streamlit as st
import ubiops 
import tempfile



st.write("streamlit example")

PROJECT_NAME = st.text_input("Project name")
API_TOKEN = st.text_input("TOKEN",type="password")
DEPLOYMENT_NAME = st.text_input("Deployment name")

api = None



configuration = ubiops.Configuration(host="https://api.ubiops.com/v2.1")
configuration.api_key['Authorization'] = API_TOKEN

client = ubiops.ApiClient(configuration)
api = ubiops.CoreApi(client)
st.write(api.service_status())

upload_file = st.file_uploader("Choose a file")
if upload_file is not None:
    st.write(upload_file)
    tf = tempfile.NamedTemporaryFile()
    tf.write(upload_file.read())
    blob = api.blobs_create(project_name=PROJECT_NAME, file=upload_file.name)
    st.write(blob)
    # Make a request using the blob id as input.
    data = {'data': blob.id}
    
    api.deployment_version_requests_create(
        project_name=PROJECT_NAME,
        deployment_name=DEPLOYMENT_NAME,
        version="v1",
        data=data
    )
