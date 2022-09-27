console.log("Script attached good to go")
URL = 'https://api.flightapi.io/onewaytrip/6329131b377b9bfe36290fcb/'

// const flightData = require("./airlines.json")
const airlineCodeMap = {
'AA' : 'American Airlines',
'JBU' : 'Jet Blue',
'UA' : 'United Airlines'
}
function getFlight(event) {
        event.preventDefault()
        const flightBody = document.querySelector("#flightBody")
        const from_flight = document.querySelector("#from_flight").value
        const to_flight = document.querySelector("#to_flight").value
        const departure_date = document.querySelector("#departure_date").value
        // const arrival_date = document.querySelector("#arrival_date").value
        fetch(URL + `${from_flight}/${to_flight}/${departure_date}/1/0/0/Economy/USD`)
				// fetch("./airlines.json")
                .then(res => res.json())
                .then(flights => {
                                const flightData = []
                                for (let i = 0; i < flights.trips.length; i++) {
                                        const trip = flights.trips[i]
                                        const tripData = {}
                                        tripData.tripId = trip.id
                                        tripData.legId = trip.legIds[0]
                                        for (let x = 0; x < flights.fares.length; x++) {
                                        	const fare = flights.fares[x]
																					if (fare.tripId === trip.id) {
																						tripData.price = fare.price.totalAmountUsd
																					}
                                        }
																				flightData.push(tripData)
                                }
																
																for (let i = 0; i < flightData.length; i++) {
																	for (let x = 0; x < flights.legs.length; x++) {
																		if (flightData[i].legId === flights.legs[x].id) {
																			flightData[i].airlineCode = flights.legs[x].airlineCodes[0]
																			flightData[i].departureTime = flights.legs[x].departureTime
																			flightData[i].arrivalTime = flights.legs[x].arrivalTime
																			flightData[i].duration = flights.legs[x].duration
																			flightData[i].stopoversCount = flights.legs[x].stopoversCount
																		}  
																	}
																}
																console.log(flightData)
                                let airlineName
																for (let i = 0; i < flightData.length; i++) {
																	if (flightData[i].airlineCode in airlineCodeMap) {
																		airlineName = airlineCodeMap[flightData[i].airlineCode]
																	} else {
																		airlineName = flightData[i].airlineCode
																	}
																	const price = flightData[i].price
                                // console.log(flights)
                                flightBody.innerHTML += `
                                <tr>    
                                        <td> ${airlineName}
                                        <td> ${flightData[i].departureTime} - ${flightData[i].arrivalTime} </td>
                                        <td>${flightData[i].duration}</td> 
                                        <td>${flightData[i].stopoversCount > 0 ? "No" : "Yes"} </td>
                                        <td>$${price.toFixed(2)}</td>
                                </tr>
                                `
                                }
                        
                })
                .catch(err => console.log(err));
}
// function getFlight(event) {
//     event.preventDefault()
//     fetch('https://travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com/v1/prices/direct/?destination=LED&origin=MOW', options)
//         .then(response => response.json())
//         .then(response => console.log(response))
//         .catch(err => console.error(err));
//     const flightResultDiv = document.querySelector("#flightResult")
//     flightResultDiv.innerHTML = 'Loading....'
//     const flightName = document.querySelector("flightName").value
//     console.log(flightName)
// }
// function getFlight(event) {
//     event.preventDefault()
//     fetch('https://travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com/v1/prices/direct/?destination=LED&origin=MOW', options)
//         .then(response => response.json())
//         .then(response => console.log(response))
//         .catch(err => console.error(err));
//     // const flightResultDiv = document.querySelector("#flightResult")
//     // flightResultDiv.innerHTML = 'Loading....'
//     // const flightName = document.querySelector("flightName").value
//     // console.log(flightName)
// }

