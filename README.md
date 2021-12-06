# Face ID

It is a project made using open source to implement Face IDs that are used in many electronic devices these days. This allows users to register faces for decryption using Haar Cascades, and then unlock only the faces they have registered.

## Result

### Save face images

Through the Haar Cascade face detector, 100 face images to be used to decrypt were stored in the designated folder. <br><br>
<img src="https://user-images.githubusercontent.com/83286706/144793485-a6e4e4cd-b1c1-44ae-9516-a43d52a2ff23.png" width="200" height="200">
<img src="https://user-images.githubusercontent.com/83286706/144793752-739728fa-5a6a-4dd6-8ef5-21d7e84231cd.png" width="200" height="200">


### Execution

Using numpy and Haar Cascade, it was executed after learning the stored image data.<br>

The face registered on Face ID<br>
<img src="https://user-images.githubusercontent.com/83286706/144795860-b33a577f-6cef-4fcc-9cf9-e78cbd0f53a7.png" width="250" height="200">

Wear a mask<br>
<img src="https://user-images.githubusercontent.com/83286706/144796523-95a9dc30-1850-4c8f-b1d0-e6ae7c37f591.png" width="250" height="200">

Face recognition failed<br>
<img src="https://user-images.githubusercontent.com/83286706/144796799-878cd24d-fd56-42a2-a15e-4e6c374feb7f.png" width="250" height="200">

someone else<br>
<img src="https://user-images.githubusercontent.com/83286706/144797061-c428dbd5-b9ea-48b9-b926-ee0bdd45d57e.png" width="250" height="200">

### Confidence
If the similarity is 85 or more, it is considered the same person as the registered face and is unlocked.<br>
However, if the similarity is less than 85, it is considered a different person and locked.

#### Reference
- https://bskyvision.com/1082
- https://velog.io/@wbsl0427/opencv%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%8B%A4%EC%8B%9C%EA%B0%84-%EC%96%BC%EA%B5%B4%EC%9D%B8%EC%8B%9D-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8-%EB%A7%8C%EB%93%A4%EA%B8%B0
- https://blog.naver.com/roboholic84/221533459586


