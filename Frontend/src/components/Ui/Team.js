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
        github:'https://github.com/GeeekySouro003',
        twitter:'https://x.com/Souradip69'
    },
    {
        imgUrl: team02,
        name: 'Abir Ghosh',
        position: 'Frontend Developer',
        linkedin:'https://www.linkedin.com/in/abir-ghosh-9aba6b2b9',
        github:'https://github.com/Abir-101',
        twitter:'https://x.com/ukeeldadu'
    },
    {
        imgUrl: team03,
        name: 'Shreemayee Saha',
        position: 'Frontend Developer and UI Designer',
        linkedin:'https://www.linkedin.com/in/sahashreemayee/',
        github:'https://github.com/techieShreee',
        twitter:'https://x.com/Shreemayee25914'
    },
    {
        imgUrl: team04,
        name: 'Promit Guha Roy',
        position: 'Applied ML Developer',
        linkedin:'https://www.linkedin.com/in/promitguharoy/',
        github:'https://github.com/promit02'
    },
];

const Team = () => {
    return (
        <section className="our__team">
            <div className="team-container">
                <div className="team__content">
                    <h6 className="subtitle"><b>Our Team</b></h6>
                    <h2>
                        Connect With{' '}
                        <span className="highlight">Us</span>
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
                                            <a href={item.twitter} target='_blank' rel="noopener noreferrer">
                                            <i className="ri-twitter-line" />
                                            </a>
                                        </span>
                                        <span>
                                            <a href={item.github} target="_blank" rel="noopener norefer">
                                            <i className="ri-github-line" />
                                            </a>
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
