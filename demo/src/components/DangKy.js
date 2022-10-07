import { useForm } from "react-hook-form";

export const DangKy = () => {
    const { register, handleSubmit, watch, formState: { errors } } = useForm();
    const onSubmit = (e, data) => {
        console.log(e, data);
    }
    console.log(watch("username"))

    return (
        <div>
            <form onSubmit={handleSubmit(onSubmit)}>
                Username: <input {...register("username")} />
                <br />

                Password:
                <input type="password" {...register("password", { required: true })} />
                {errors.password && <span>This field is required</span>}
                <br />

                <input {...register("firstName", { required: true, maxLength: 20 })} /><br />

                <input {...register("lastName", { pattern: /^[A-Za-z]+$/i })} />
                {errors.lastName && <span>Only character</span>}
                <br />

                <input type="number" {...register("age", { min: 18, max: 60 })} />
                {errors.age && <span>Age from 18 - 60</span>}
                <br />
                <input type="submit" value="Register" />
            </form>
        </div>
    )
}