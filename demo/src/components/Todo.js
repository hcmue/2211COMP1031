import { useContext } from "react";
import { VerticalTimeline, VerticalTimelineElement } from 'react-vertical-timeline-component';
import 'react-vertical-timeline-component/style.min.css';
import { TodoContext } from "../contexts/TodoContext";
import { ReactComponent as WorkIcon } from './work.svg';


export const Todo = () => {
    const { tasks } = useContext(TodoContext);

    return (
        <>
            <h2>TODOs</h2>
            <VerticalTimeline>
                {tasks.map((item) => {
                    return (
                        <VerticalTimelineElement
                            key={item.id}
                            date={item.deadline}
                            className="vertical-timeline-element--work"
                            iconStyle={{ background: "rgb(33, 150, 243)", color: "#fff" }}
                            contentStyle={{ color: "rgb(33, 150, 243)", background: "#fff" }}
                            contentArrowStyle={{ borderRight: "7px solid  rgb(33, 150, 243)" }}
                            icon={<WorkIcon />}
                        >
                            <h3 className="vertical-timeline-element-title">
                                {item.name}
                            </h3>
                            {!item.isCompleted && (
                                <button style={{ padding: 9, margin: 3, backgroundColor: '#06d6a0', color: 'white' }}>
                                    Complete
                                </button>
                            )}
                        </VerticalTimelineElement>
                    )
                })}
            </VerticalTimeline>
        </>
    )
}