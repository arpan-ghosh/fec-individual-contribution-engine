[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="https://upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/800px-Flag_of_the_United_States.svg.png" alt="Logo" width="80" height="80">

  <h3 align="center">Federal Election Committee Big Data Collection</h3>

  <p align="center">
    FEC API Queries using GraphQL and Golang
  </p>
</p>



<!-- ABOUT THE PROJECT -->
## About The Project 

This is a work in progress.

The main goal of this project is to showcase Golang, Python, and REST + GraphQL expertise. I'm also interested to find out how well the Go implementation  does at crunching incredibly large queries using concurrent channels.

Specifically though, this project maps political affiliation of the Indian American demographic. We can do this by isolating for South Asian names, provided in a CSV corpus.
This is just one application, you can isolate other demographics, and filter based on a multitude of factors including zip code, commitetes, dates, campaign finance data efilings, etc. and make inferences by analyzing the data returned. Feel free to browse their API here https://api.open.fec.gov/developers/.

In this example we are just counting South Asian surnames, associating them to a candidate by using regular expressions to find candidate, PAC, or commitee support, and categorizing by state. You can start to see why this can be a very powerful tool, and why certain entities may want to do this type of analysis. I'll be making an API call to the api.open.fec.gov/v1/schedules/schedule_a/ endpoint since I care about data at the individual donor level.

### Built With

* [Go](https://golang.org/)
* [GraphQL](https://graphql.org/)
* [MongoDB](https://www.mongodb.com/)


<!-- GETTING STARTED -->
## Getting Started
Download the repository and run the following to play around with entering data into a MongoDB. This assumes that you have mongodb installed and running on your host.

#### Then follow these steps to run the server:
```
cd fec-individual-contribution-engine/go/graphql/graph
go run server.go 
```
#### If you make changes to the schema, you can generate all the code needed thanks to 99Designs:
```
cd fec-individual-contribution-engine/go/graphql/graph`
go run github.com/99designs/gqlgen
```

### Prerequisites

To get MongoDB hosted on your localhost to port 27017 follow these steps (MacOS/Unix/Linux):
```
brew tap mongodb/brew
brew install mongodb-community@4.4
brew services start mongodb-community@4.4
dep ensure --add go.mongodb.org/mongo-driver/mongo \\ngo.mongodb.org/mongo-driver/bson \\ngo.mongodb.org/mongo-driver/mongo/options\n
mongo
```

You'll get something like this:

```
arpanghosh@Arpans-MBP graphql % mongo
MongoDB shell version v4.4.1
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("01a60b57-2e51-4d89-87a8-0e642274bde5") }
MongoDB server version: 4.4.1
```

### Installation

1. TBD


<!-- USAGE EXAMPLES -->
## Usage

Useful examples, aditional screenshots, code examples and demos are in the works. Stay tuned.


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Arpan Ghosh - arpanghosh95@gmail.com
Project Link: [https://github.com/arpan-ghosh/fec-individual-contribution-engine](https://github.com/arpan-ghosh/fec-individual-contribution-engine)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/arpanghosh
