import axios from "axios";

const baseUrl = "http://localhost:8000"

export function getPassword(body, setPassword){
    axios.get(`${baseUrl}/password/generate`,{ params: body })
      .then(function (response) {
        setPassword(response.data)
      })
      .catch(function (error) {
        console.log(error);
      })
      .finally(function () {
        // always executed
      });
}

// , {
//     params: body
//   }
