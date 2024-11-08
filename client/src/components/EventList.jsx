import React, { useEffect, useState } from 'react';
import api from '../api'; 

const EventList = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    const fetchEvents = async () => {
      try {
        const response = await api.get('/events');
        setEvents(response.data);
        console.log("Events fetched:", response.data);
      } catch (error) {
        console.error("Error fetching events:", error);
      }
    };
    const intervalId = setInterval(fetchEvents, 3000);

    return () => clearInterval(intervalId);
  }, []);

  return (
    <div>
      <h2 className="text-center mt-4">Event Tracking Details</h2>
      <div className="row">
        {Array.isArray(events) && events.length > 0 ? (
          events.map(event => (
            <div key={event.id} className="col-md-4 mb-4">
              <div className="card">
                <img src={`${api.defaults.baseURL}/image/${event.annotatedImage}`} className="card-img-top" alt={`Event ${event.id}`} />
                <div className="card-body">
                  <h5 className="card-title">Classified Person: {event.classified_person}</h5>
                  <p className="card-text"><small className="text-muted">{new Date(event.timestamp).toLocaleString()}</small></p>
                </div>
              </div>
            </div>
          ))
        ) : (
          <p>No events found.</p>
        )}
      </div>
    </div>
  );
};

export default EventList;
