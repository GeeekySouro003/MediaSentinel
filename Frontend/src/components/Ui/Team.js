import React from 'react';
import '../Ui/team.css';
import team01 from '../../images/team-01.jpeg';
import team02 from '../../images/team-02.jpg';
import team03 from '../../images/team-03.png';
import team04 from '../../images/team-04.png';

const teamMembers = [
    {
        imgUrl: team01,
        name: 'Souradip Dasgupta',
        position: 'Backend and ML Platform Developer',
        linkedin: 'https://www.linkedin.com/in/souradip-dasgupta',
    },
    {
        imgUrl: team02,
        name: 'Abir Ghosh',
        position: 'Frontend Developer',
    },
    {
        imgUrl: team03,
        name: 'Shreemayee Saha',
        position: 'Frontend Developer and UI Designer',
    },
    {
        imgUrl: team04,
        name: 'Promit Guha Roy',
        position: 'Applied ML Developer',
    },
];

const Team = () => {
    return (
        <section className="our__team">
            <div className="container">
                <div className="team__content">
                    <h6 className="subtitle">Our Team</h6>
                    <h2>
                        Join With{' '}
                        <span className="highlight">Our Team</span>
                    </h2>
                    <div className="team__wrapper">
                        {teamMembers.map((item, index) => (
                            <div className="team__item" key={index}>
                                <div className="team__img">
                                    <img src={item.imgUrl} alt={item.name} />
                                </div>
                                <div className="team__details">
                                    <h4>{item.name}</h4>
                                    <p className="description">{item.position}</p>
                                    <div className="team__member-social">
                                        {item.linkedin && (
                                            <span>
                                                <a href={item.linkedin} target="_blank" rel="noopener noreferrer">
                                                    <i className="ri-linkedin-line" />
                                                </a>
                                            </span>
                                        )}
                                        <span>
                                            <i className="ri-twitter-line" />
                                        </span>
                                        <span>
                                            <i className="ri-facebook-line" />
                                        </span>
                                    </div>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </section>
    );
};

export default Team;
