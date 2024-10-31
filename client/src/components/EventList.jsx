import React, { useEffect, useState } from 'react';
import api from '../api'; 

const EventList = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    const fetchEvents = async () => {
      try {
        const response = await api.get('/events');
        console.log(response.data); // Check the response data
        setEvents(response.data);
      } catch (error) {
        console.error("Error fetching events:", error);
      }
    };
    fetchEvents();
  }, []);

  return (
    <div>
      <h2 className="text-center mt-4">Uploaded Events</h2>
      <div className="row">
        {Array.isArray(events) && events.length > 0 ? (
          events.map(event => (
            <div key={event.id} className="col-md-4 mb-4">
              <div className="card">
                <img src={`/image/${event.image_path}`} className="card-img-top" alt={`Event ${event.id}`} />
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